// https://pokeapi.co/api/v2/pokemon/1/

// Promisse = Promessa

let currentIndex = 1
const nextButton = document.querySelector('#next')
const previousButton = document.querySelector('#previous')

const male = document.querySelector('#male')
const female = document.querySelector('#female')

let gender = 'male';
const input = document.querySelector('#input')

const typeColors = {
    normal: "#A8A77A",
    fire: "#EE8130",
    water: "#6390F0",
    electric: "#F7D02C",
    grass: "#7AC74C",
    ice: "#96D9D6",
    fighting: "#C22E28",
    poison: "#A33EA1",
    ground: "#E2BF65",
    flying: "#A98FF3",
    psychic: "#F95587",
    bug: "#A6B91A",
    rock: "#B6A136",
    ghost: "#735797",
    dragon: "#6F35FC",
    dark: "#705746",
    steel: "#B7B7CE",
    fairy: "#D685AD"
};

async function fetchPokemonData(id) {
    let requisition = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}/`);
    let json = await requisition.json();

    let h1_name = document.querySelector('#name');
    h1_name.textContent = json.name;

    let h1_id = document.querySelector('h1#id');
    h1_id.textContent = '#' + json.id;

    let pokemonImage = document.querySelector('#pokemon_image');

    if (gender == 'male'){
        pokemonImage.src = json.sprites.other.home.front_default;
    }else{
        pokemonImage.src = json.sprites.other.home.front_female;
    }

    let typesContainer = document.querySelector('.types');
    typesContainer.innerHTML = '';

    let primaryType = json.types[0].type.name;


    document.body.style.backgroundColor = typeColors[primaryType] || "#FFF";

    json.types.forEach((typeInfo) => {
        let typeElement = document.createElement("h1");
        typeElement.textContent = typeInfo.type.name;

        typeElement.style.backgroundColor = typeColors[typeInfo.type.name];
        typeElement.style.color = "#FFF";
        typeElement.style.padding = "5px 10px";
        typeElement.style.borderRadius = "10px";
        typeElement.style.display = "inline-block";
        typeElement.style.margin = "5px";

        typesContainer.appendChild(typeElement);
    });
}

nextButton.addEventListener('click', () => {
    currentIndex++;
    fetchPokemonData(currentIndex);
});

previousButton.addEventListener('click', () => {
    if (currentIndex <= 1) {
        alert('You are on the last pokemon')
    } else {
        currentIndex--;
        fetchPokemonData(currentIndex);
    }
});

input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        if (input.value <= 0) {
            alert('You entered a value out of range')
        }
        currentIndex = input.value
        fetchPokemonData(input.value)
        input.value = ''
    }
})

male.addEventListener('click', () => {
    gender = 'male';
    console.log(gender)

})

female.addEventListener('click', () => {
    gender = 'female'
    console.log(gender)

})

fetchPokemonData(currentIndex);