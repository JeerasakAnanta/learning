function greet(name) {
  console.log("Output: " + name);
}

function add(a, b) {
  console.log("sout a + b ", a + b);
}
// greet("Game");

add(1, 10);

/* anoymous function s a function s that dows not have a name
 to a variable  or use a callback .Since  it hos no name 
 
 */

const greet2 = function () {
  return " HI there!";
};

// console.log("greet2", greet2());

const add2 = function (a, b) {
  return a + b;
};
console.log("add function ", add2(1, 20));

/* arrow function se6
 a new way to write function using the => sysntax  they are shorter 
 and  do not have their won the  boinding whic make them usful in somase  

 */
const squere = (n) => n * n;
console.log("call  squere", squere(10));

/* Immediately  invoked function sexmpoerssion  
iffe functions are executed immdedately aftertheir  definition  
sthey are often   used tocreate isolated  scopes */

(function () {
  console.log("this runs immediately!");
})();

/* callback  function a callbak function is  */

function num(n, callback) {
  return callback(n);
}

const dubile = (n) => n * 2;

/* fAsync Function 
function that handle asynchornous thask  declared    with async thery return a pormse
and you can use  awit indside hem to pause promise  resolves */

console.log("-------------- Asnc Function -------------- ");
async function fechData() {
  return "data fecthed!";
}
fechData().then(console.log);


/* declared  with an asterisk  these function  can  pause  execution using
yield  and resume laster. useful for  lazy loading velues or  handling iterators */
console.log("-------------- Generator Function -------------- ");
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = numbers();
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2

