<p>
  <img alt="logo" src"11photo\ logo.png" />
</p>
<h1 align="center">
  Welcome to 11Photo 👋
</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: ISC" src="https://img.shields.io/badge/License-ISC-yellow.svg" />
  </a>
</p>

> A photo essay generator using 11ty, pug and tailwind

## Getting Started
*   clone the repo.
*   copy the `template` folder, and rename it.
*   inside of the new folder, find the file `template.json`, rename it to the same name as your folder.
*   chuck all your photos into the `photos` foler
*   run `npx tailwindcss build src.css -o dist.css` to generate the css.
*   after you've done all that, run `npx @11ty/eleventy`
## Changing the colours:
changing colours can be done by altering the variables in the `tailwind.config file`. and then running `npx tailwindcss build src.css -o dist.css`.
At the moment there is no way to change the colours specifically for one essay.
## Author

👤 **Darcy Lugt-Falk**

* Website: darcylf.me
* Github: [@ehne](https://github.com/ehne)

## Show your support

Give a ⭐️ if this project helped you!

> the photo used in the example is by chuttersnap on Unsplash
***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
