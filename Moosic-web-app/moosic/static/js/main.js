const showSignUp = () => {
    const form = document.querySelector("#sign-up-form");
    form.style.zIndex = 1000;
    form.hidden = false;

}

const showLogIn = () => {
    const form = document.querySelector("#log-in-form");
    form.style.zIndex = 1000;
    form.hidden = false;

}

//function for finding user input genre ands mood goal
const findGenreMood = () => [...document.querySelectorAll('div.carousel-item.active text')].map(el => el.textContent);

//function to load the site that shows interim predictions
const loadInterimResults = () => {
    const [genre, mood] = findGenreMood();
    //postData('/predict', {genre: genre, mood: mood})
    const url = `/result?genre=${genre}&mood=${mood}`;
    window.open(url);
}

// source: https://www.geeksforgeeks.org/javascript-post-request-like-a-form-submit/
// only method parameter removed, because it's always POST for us.
// call as: postData("/predict", { genre: "Jazz", mood: "Happy" })
const postData = (path, params) => {

    // Create form
    const hidden_form = document.createElement('form');

    // Set method to post by default
    hidden_form.method = 'post';

    // Set path
    hidden_form.action = path;

    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hidden_input = document.createElement('input');
            hidden_input.type = 'hidden';
            hidden_input.name = key;
            hidden_input.value = params[key];
            hidden_form.appendChild(hidden_input);
        }
    }

    document.body.appendChild(hidden_form);
    hidden_form.submit();
}