'use strict';

const form = document.getElementById('searchForm');
const input = document.getElementById('query');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent normal form submission

    const query = input.value.trim();
    if (!query) {
        alert('Please enter a TV series name');
        return;
    }

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
        if (!response.ok) throw new Error('Network error');

        const data = await response.json();

        resultsDiv.innerHTML = '';

        data.forEach(item => {
            const tvShow = item.show;

            const article = document.createElement('article');

            const h2 = document.createElement('h2');
            h2.textContent = tvShow.name;
            article.appendChild(h2);

            const a = document.createElement('a');
            a.href = tvShow.url;
            a.textContent = 'Details';
            a.target = '_blank';
            article.appendChild(a);

            if (tvShow.image?.medium) {
                const img = document.createElement('img');
                img.src = tvShow.image.medium;
                img.alt = tvShow.name;
                article.appendChild(img);
            }

            const summaryDiv = document.createElement('div');
            summaryDiv.innerHTML = tvShow.summary || 'No summary available';
            article.appendChild(summaryDiv);

            resultsDiv.appendChild(article);
        });

    } catch (error) {
        console.error('Error fetching data:', error);
        resultsDiv.innerHTML = '<p>Error fetching data. Please try again later.</p>';
    }
});
