function renderChart(hours, levels) {
    const ctx = document.getElementById('lightChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: hours,
            datasets: [{
                label: 'Light Level',
                data: levels,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
                fill: false
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Hour'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Light Level'
                    }
                }
            }
        }
    });
}