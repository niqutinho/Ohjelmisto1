'use strict';

const form = document.getElementById('searchForm');
const input = document.getElementById('query');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent form from submitting normally

    const query = input.value.trim();
    if (!query) {
        console.log('Please enter a TV series name');
        return;
    }

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error('Network error');

        const data = await response.json();
        console.clear(); // Clear previous results
        console.log(data); // Print full JSON

        // Optional: print a clean summary in the console
        data.forEach(item => {
            console.log('Title:', item.show.name);
            console.log('Genres:', item.show.genres.join(', ') || 'N/A');
            console.log('Summary:', item.show.summary ? item.show.summary.replace(/<[^>]+>/g, '') : 'N/A');
            console.log('---');
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
