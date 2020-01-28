<p>
  <img alt="logo" src="11photo-logo.png" align="center"/>
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
*   chuck all your photos into the `photos` folder. nb: the image `hero.jpg` is by default, the hero image used on the site (this can be edited in the json file)
*   from inside the folder, run the `generator.py` script. this will generate the json data file.
*   open the json file, and edit the data to be what you want. ie. the captions of images, and title of the essay.
*   run `npm run build` to build the website into the `_site` directory.
*   if you encounter any problems, be sure to make an issue on github.
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
