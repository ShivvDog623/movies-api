


// MY WAY OF DOING IT
// -------------------------------------------
const createMovieForm = document.getElementById('createMovieForm')
const createActorForm = document.getElementById('createActorForm')
const createGenreForm = document.getElementById('createGenreForm')
const createDirectorForm = document.getElementById('createDirectorForm')
const base_url = "http://localhost:5000"


/**
 * Global Function
 */

function resetAction() {
    alert("Page will reload: Data entered will be lost")
    createMovieForm.reset();
    createActorForm.reset();
    createGenreForm.reset();
    createDirectorForm.reset();
}

/*---------------------------------------------------------------MOVIE------------------------------------------------------------*/

/**
 * GET request for all movies from API
 */
const getAllMovies = async () => {
    const movie_all_url = `${base_url}/movies/all`
    const response = await fetch(movie_all_url, {
        method: 'GET'
    })

    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    populateMovieTable(data);
};

/**
 * Will populate the table with movie data from the GET request 
 * @param {dictionary} data - unique modal identifier
 */
const populateMovieTable = async (data) => {
    const movieData = data.data;
    const limit = 5
    let movieTable = document.getElementById('movieTable');
    let out = "";

    for (i = 0; i < movieData.length && i < limit; i++) {
        const movie = movieData[i]
        const { title, year, description, time, movie_id } = movie
        out = `${out}
                        <tr>
                            <td scope="row" class="p-4 col-1">
                                <a href="#" id="movieLink" onclick="populateMovieModal(${movie_id})">
                                <i class="bi bi-binoculars-fill"></i>
                                </a>
                            </td>
                            <td scope="row" class="p-3">${title}</td>
                            <td scope="row" class="p-3">${year}</td>
                            <td scope="row" class="p-3">${description}</td>
                            <td scope="row" class="p-3">${time}</td>
                        </tr>`
        movieTable.innerHTML = out;
    }
}

/**
 * GET request for movie by Id from API
 * @param {string} movie_id - unique modal identifier
 */
const getMoviesByID = async (movie_id) => {
    const movie_id_url = `${base_url}/movies/${movie_id}`
    const response = await fetch(movie_id_url, {
        method: 'GET'

    })

    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    return data
};

/**
 * Will populate the modal with movie data
 * @param {int} movie_id - unique modal identifier
 */

const populateMovieModal = async (movie_id) => {
    const data = await getMoviesByID(movie_id);
    var movieIDData = data.data
    const movie = movieIDData[0];
    const { title, year, description, time, rating, vote, revenue, metascore } = movie
    let modalGetHeader = document.getElementById('get-modal-header')
    modalGetHeader.innerHTML = `
                                        <p class="modal-title"><strong>Title: ${title} 
                                        <br>
                                        Year: ${year}</strong></p>
                                        <button id="modalClose" type="button" class="btn-close"  aria-label="Close" onclick="closeModal('get-modal')"></button>
                                        `
    let modalGetBody = document.getElementById('get-modal-body')
    modalGetBody.innerHTML = ` <p>
                                        <strong>Description:</strong> ${description}
                                        <br>
                                        <strong>Time:</strong> ${time}
                                        <br>
                                        <strong>Rating:</strong> ${rating}
                                        <br>
                                        <strong>Vote:</strong> ${vote}
                                        <br>
                                        <strong>Revenue:</strong> ${revenue}
                                        <br>
                                        <strong>Metascore:</strong> ${metascore}
                                        <br>

                                    </p>`
    openModal('get-modal');
}

/**
 * 'POST' request
 * @param {dictionary} newMovie - gets newMovie payload to use for 'POST' request
 */
const createMovie = async (newMovie) => {
    const movie_post_url = `${base_url}/movies/create`
    const response = await fetch(movie_post_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newMovie)
    });
    const data = await response.json();

    if (!response.ok) {
        console.log(data.description);
        return;
    }
}

/**
 * Will get payload for POST movies request
 */
function submitMovie() {
    const title = document.getElementById("title").value;
    const year = document.getElementById("year").value;
    const description = document.getElementById("description").value;
    const time = document.getElementById("time").value;
    var rating = document.getElementsByName('radio1');
    let ratings;

    for (r = 0; r < rating.length; r++) {
        if (rating[r].checked)
            ratings = rating[r].value
    }

    const votes = document.getElementById("votes").value;
    const revenue = document.getElementById("revenue").value;
    const metascore = document.getElementById("metascore").value;
    const newMovie = {
        'title': `${title}`,
        "year": `${year}`,
        "description": `${description}`,
        "time": `${time}`,
        "rating": `${ratings}`,
        "vote": `${votes}`,
        "revenue": `${revenue}`,
        "metascore": `${metascore}`
    }
    createMovie(newMovie)
        .then(data => {
            console.log('movie submitted')
        })
        .catch(error => {
            console.log(error);
        })

    console.log(title)
}

/**
 * Will hide and show divs when clicked on front end side
 * @param {string} divId - unique modal identifier
 */
function loadDiv(divId) {
    var showDiv = document.getElementById(divId);
    const menuItems = ['divMovies', 'divActors', 'divDirectors', 'divGenres']
    for (const item of menuItems) {
        const ele = document.getElementById(item)
        ele.style.display = 'none'
    }

    if (divId === 'divMovies') {
        showDiv.style.display = 'block'
        getAllMovies();
    }

    if (divId === 'divActors') {
        showDiv.style.display = 'block'
        getAllActors();

    }

    if (divId === 'divGenres') {
        showDiv.style.display = 'block'
        getAllGenres();

    }

    if (divId === 'divDirectors') {
        showDiv.style.display = 'block'
        getAllDirectors();
    }
}

/*---------------------------------------------------------------ACTOR------------------------------------------------------------*/

/**
 * GET request for actors from API
 */
const getAllActors = async () => {
    const actor_all_url = `${base_url}/actor/all`
    const response = await fetch(actor_all_url, {
        method: 'GET'
    })

    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    populateActorTable(data);
};

const populateActorTable = async (data) => {
    const actorData = data.data;
    const limit = 5
    let actorTable = document.getElementById('actorTable')
    let out = "";

    for (i = 0; i < actorData.length && i < limit; i++) {
        const actor = actorData[i]
        const { first_name, middle_name, last_name, actor_id } = actor
        out = `${out}
                        <tr>
                            <td scope="row" class="p-4 col-1">
                                <a href="#" id="actorLink" onclick="populateActorModal(${actor_id})">
                                <i class="bi bi-binoculars-fill"></i>
                                </a>
                            </td>
                            <td scope="row" class="p-3 col-2">${first_name}</td>
                            <td scope="row" class="p-3 col-2">${middle_name}</td>
                            <td scope="row" class="p-3 col-2">${last_name}</td>
                        </tr>`
        actorTable.innerHTML = out;

    }
}

/**
 * GET request for actor by Id from API
 * @param {string} actor_id - unique modal identifier
 */
const getActorsByID = async (actor_id) => {
    const movie_id_url = `${base_url}/actor/${actor_id}`
    const response = await fetch(movie_id_url, {
        method: 'GET'
    })

    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    return data
};

/**
 * Will populate the modal with actor data
 * @param {int} actor_id - unique modal identifier
 */
const populateActorModal = async (actor_id) => {
    const data = await getActorsByID(actor_id)
    var actorIDData = data.data
    const actor = actorIDData[0];
    const { first_name, middle_name, last_name } = actor
    let modalGetHeader = document.getElementById('get-modal-header')
    modalGetHeader.innerHTML = `
                                <h4 class="modal-title">Genre Info</h4>
                                <button id="modalClose" type="button" class="btn-close"  aria-label="Close" onclick="closeModal('get-modal')"></button>
                                `
    let modalGetBody = document.getElementById('get-modal-body')
    modalGetBody.innerHTML = ` <p>
                                        <strong>First Name:</strong> ${first_name}
                                        <br>
                                        <strong>Middle Name:</strong> ${middle_name}
                                        <br>
                                        <strong>Last Name:</strong> ${last_name}
                                    </p>`

    openModal('get-modal');
}

/**
 * 'POST' request
 * @param {dictionary} newActor - gets newActor payload to use for 'POST' request
 */
const createActor = async (newActor) => {
    const movie_post_url = `${base_url}/actor/create`
    const response = await fetch(movie_post_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',

        },
        body: JSON.stringify(newActor)
    });
    const data = await response.json();

    if (!response.ok) {
        console.log(data.description);
        return;
    }
}

/**
 * Will get payload for POST actors request
 */
const submitActor = async () => {
    const data = await createActor(newActor)
    const first_name = document.getElementById("actorFirstName").value;
    const middle_name = document.getElementById("actorMiddleName").value;
    const last_name = document.getElementById("actorLastName").value;
    const newActor = {
        "first_name": `${first_name}`,
        "middle_name": `${middle_name}`,
        "last_name": `${last_name}`
    }
    createActor(newActor)
        .then(data => {
            console.log('actor submitted')
        })
        .catch(error => {
            console.log(error)
        })
}

/*---------------------------------------------------------------GENRE------------------------------------------------------------*/

/**
 * GET request for all movies from API
 */
const getAllGenres = async () => {
    const genre_all_url = `${base_url}/genre/all`
    const response = await fetch(genre_all_url, {
        method: 'GET'
    })

    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    populateGenreTable(data);
};

const genreResults = document.getElementById('genreData');

/**
 * Will populate the table with genre data from the GET request 
 * @param {dictionary} data - unique modal identifier
 */
const populateGenreTable = async (data) => {
    const genreData = data.data;
    const limit = 5
    let genreTable = document.getElementById('genreTable');
    let out = "";

    for (i = 0; i < genreData.length && i < limit; i++) {
        const genre_data = genreData[i]
        const { genre, genre_id } = genre_data
        out = `${out}
                        <tr>
                            <td scope="row" class="p-3 col-2">
                                <a href="#" id="genreLink" onclick="populateGenreModal(${genre_id})">
                                <i class="bi bi-binoculars-fill"></i>
                                </a>
                            </td>
                            <td scope="row" class="p-3 col-2">${genre}</td>
                        </tr>`
        genreTable.innerHTML = out;
    }
}

/**
 * GET request for genre by Id from API
 * @param {string} genre_id - unique modal identifier
 */
const getGenresByID = async (genre_id) => {
    const genre_id_url = `${base_url}/genre/${genre_id}`
    const response = await fetch(genre_id_url, {
        method: 'GET'

    })

    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    return data
};

/**
 * Will populate the modal with genre data
 * @param {int} genre_id - unique modal identifier
 */

const populateGenreModal = async (genre_id) => {
    const data = await getGenresByID(genre_id)

    var genreIDData = data.data
    const genre_data = genreIDData[0];
    const { genre } = genre_data
    let modalGetHeader = document.getElementById('get-modal-header')
    modalGetHeader.innerHTML = `<h4 class="modal-title">Genre Info</h4>
                                <button id="modalClose" type="button" class="btn-close"  aria-label="Close" onclick="closeModal('get-modal')"></button>
                                `

    let modalGetBody = document.getElementById('get-modal-body')
    modalGetBody.innerHTML = ` <p>
                                <strong>Genre:</strong> ${genre}
                                <br>
                            </p>`
    openModal('get-modal');
}

/**
 * 'POST' request
 * @param {dictionary} newGenre - gets newGenre payload to use for 'POST' request
 */
const createGenre = async (newGenre) => {
    const genre_post_url = `${base_url}/genre/create`
    const response = await fetch(genre_post_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newGenre)
    });
    const data = await response.json();

    if (!response.ok) {
        console.log(data.description);
        return;
    }
}

/**
 * Will get payload for POST genres request
 */

function submitGenre() {
    const genre = document.getElementById("genre").value
    const newGenre = {
        "genre": `${genre}`,

    }
    createGenre(newGenre)
        .then(data => {
            console.log('genre submitted')
        })
        .catch(error => {
            console.log(error)
        })
}

/*---------------------------------------------------------------DIRECTORS------------------------------------------------------------*/

/**
 * GET request for directors from API
 */

const getAllDirectors = async () => {

    const director_all_url = `${base_url}/directors/all`
    const response = await fetch(director_all_url, {
        method: 'GET'
    })


    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();
    populateDirectorTable(data);
};

/**
 * Will populate the table with director data from the GET request 
 * @param {dictionary} data - unique modal identifier
 */

function populateDirectorTable(data) {
    const directorData = data.data;

    const limit = 5
    let directorTable = document.getElementById('directorTable')
    let out = "";

    for (i = 0; i < directorData.length && i < limit; i++) {
        const director = directorData[i]
        const { first_name, middle_name, last_name, director_id } = director
        out += `
                        <tr>
                            <td scope="row" class="p-4 col-1">
                                <a href="#" id="directorLink" onclick="populateDirectorModal(${director_id})">
                                <i class="bi bi-binoculars-fill"></i>
                                </a>
                            </td>
                            <td scope="row" class="p-3 col-2">${first_name}</td>
                            <td scope="row" class="p-3 col-2">${middle_name}</td>
                            <td scope="row" class="p-3 col-2">${last_name}</td>
                        </tr>`
        directorTable.innerHTML = out;
    }
}

/**
 * GET request for director by Id from API
 * @param {string} director_id - unique modal identifier
 */
const getDirectorByID = async (director_id) => {
    const director_id_url = `${base_url}/directors/${director_id}`
    const response = await fetch(director_id_url, {
        method: 'GET'

    })


    if (response.status !== 200) {
        throw new Error('cannot fetch the data')
    }

    const data = await response.json();

    return data
};

/**
 * Will populate the modal with director data
 * @param {int} director_id - unique modal identifier
 */

const populateDirectorModal = async (director_id) => {
    const data = await getDirectorByID(director_id)
    var directorIDData = data.data
    const director = directorIDData[0];
    const { first_name, middle_name, last_name } = director
    let modalGetHeader = document.getElementById('get-modal-header')
    modalGetHeader.innerHTML = `
                                        <h4 class="modal-title">Director Info</h4>
                                        <button id="modalClose" type="button" class="btn-close"  aria-label="Close" onclick="closeModal('get-modal')"></button>
                                        `

    let modalGetBody = document.getElementById('get-modal-body')
    modalGetBody.innerHTML = ` <p>
                                        <strong>First Name:</strong> ${first_name}
                                        <br>
                                        <strong>Middle Name:</strong> ${middle_name}
                                        <br>
                                        <strong>Last Name:</strong> ${last_name}
                                        <br>
                                    </p>`

    openModal('get-modal');

}

/**
 * 'POST' request
 * @param {dictionary} newDirector - gets newDirector payload to use for 'POST' request
 */
const createDirector = async (newDirector) => {
    const director_post_url = `${base_url}/directors/create`
    const response = await fetch(director_post_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',

        },
        body: JSON.stringify(newDirector)
    });
    const data = await response.json();

    if (!response.ok) {
        console.log(data.description);
        return;
    }

}

/**
 * Will get payload for POST directors request
 */

function submitDirector() {
    const first_name = document.getElementById("directorFirstName").value;
    const middle_name = document.getElementById("directorMiddleName").value;
    const last_name = document.getElementById("directorLastName").value;

    const newDirector = {
        "first_name": `${first_name}`,
        "middle_name": `${middle_name}`,
        "last_name": `${last_name}`
    }

    createDirector(newDirector)
        .then(data => {
            console.log('director submitted')
        })
        .catch(error => {
            console.log(error)
        })

}

/**
 * It opens a modal window
 * @param {string} modalId - unique modal identifier
 */
function openModal(modalId) {
    var modalOpen = new bootstrap.Modal(document.getElementById(modalId))
    if (modalOpen) {
        modalOpen.show();
    }
}

/**
 * It closes a modal window
 * @param {string} modalId - unique modal identifier
 */
function closeModal(modalId) {
    var modalClose = bootstrap.Modal.getInstance(document.getElementById(modalId))
    if (modalClose) {
        modalClose.hide();
    }
}