function startFriday() {
    window.location.href = '/start_friday';
}

window.addEventListener('load', function() {
    const loadingBox = document.getElementById('loading-box');
    const dataBox = document.getElementById('data-box');
    
    if (loadingBox && dataBox) {
        setTimeout(() => {
            loadingBox.classList.add('d-none');
            dataBox.classList.remove('d-none');
            fetchData();
        }, 3000);
    }
});

function fetchData() {
    fetch('/page2/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('data-box').innerText = data.output;
        })
        .catch(error => console.error('Error:', error));
}
