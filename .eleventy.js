module.exports = function(eleventyConfig) {
    // Find and copy any `jpg` files, maintaining directory structure.
    eleventyConfig.setTemplateFormats([
        "pug",
        "png",
        "jpg" // css is not yet a recognized template extension in Eleventy
      ]);
    eleventyConfig.addPassthroughCopy("./dist.css");
  };
