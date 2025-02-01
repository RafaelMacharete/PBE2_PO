// https://pokeapi.co/api/v2/pokemon/1/

// Promisse = Promessa

let currentIndex = 1
const nextButton = document.querySelector('#next')

async function fetchPokemonData(id) {
    let requisition = await (fetch(`https://pokeapi.co/api/v2/pokemon/${id}/`));
    let json = await requisition.json();

    h1_name = document.querySelector('#name');
    h1_name.textContent = json.name;

    let pokemonImage = document.querySelector('#pokemon_image');
    pokemonImage.src = json.sprites['front_default'];
}

nextButton.addEventListener('click', () => {
    currentIndex++; 
    fetchPokemonData(currentIndex);
});

fetchPokemonData(currentIndex);