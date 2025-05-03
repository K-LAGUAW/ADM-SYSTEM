const inputs = document.querySelectorAll('#addModal input, #addModal select');
const provinceSelect = document.getElementById('provinceSelect');
const localitySelect = document.getElementById('localitySelect');

addModal.addEventListener('show.bs.modal', () => {
    provinceSelect.disabled = true;
    localitySelect.disabled = true;

    const provincesApi = 'https://apis.datos.gob.ar/georef/api/provincias?campos=id,nombre';

    fetch(provincesApi)
        .then(response => response.json())
        .then(data => {
            const provinces = data.provincias.sort((a, b) => a.nombre.localeCompare(b.nombre));

            provinces.forEach(provincia => {
                const option = document.createElement('option');
                option.id = provincia.id;
                option.textContent = provincia.nombre;
                provinceSelect.appendChild(option);
            });

            provinceSelect.selectedIndex = -1;

            provinceSelect.disabled = false;
        })
        .catch(error => {
            console.error('Error:', error);
            provinceSelect.disabled = true;
            provinceSelect.className = 'form-select is-invalid';
        });

    provinceSelect.addEventListener('change', function () {
        const provinceId = this.value;

        const localitiesApi = `https://apis.datos.gob.ar/georef/api/municipios?provincia=${provinceId}&campos=id,nombre&max=100`;

        fetch(localitiesApi)
            .then(response => response.json())
            .then(data => {
                localitySelect.innerHTML = '';
                const localities = data.municipios.sort((a, b) => a.nombre.localeCompare(b.nombre));

                localities.forEach(localidad => {
                    const option = document.createElement('option');
                    option.id = localidad.id;
                    option.textContent = localidad.nombre;
                    localitySelect.appendChild(option);
                });
                
                localitySelect.selectedIndex = -1;

                localitySelect.disabled = false;
            })
            .catch(error => {
                console.error('Error:', error);
                localitySelect.disabled = true;
                localitySelect.className = 'form-select is-invalid';
            });
    });
})

addModal.addEventListener('hide.bs.modal', () => {
    inputs.forEach(input => {
        if (input.tagName == 'SELECT') {
            input.innerHTML = '';
        } else {
            input.value = '';
        }
        input.classList.remove('is-invalid');
    });
});