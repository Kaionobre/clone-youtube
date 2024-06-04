
document.getElementById('thumb').addEventListener('click', function() {
    document.getElementById('id_thumbnail').click();
});

document.getElementById('id_video').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        console.log('Arquivo selecionado:', file.name);
    }
});
