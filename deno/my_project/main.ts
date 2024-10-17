function capitalize(word) {
  return word.charAt(0).toUpperCase() + word.slice(1);
}

function hello(name :string) {
  return "Hello " + capitalize(name);
}
