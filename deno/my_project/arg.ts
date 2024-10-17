console.log(Deno.args);

if (Deno.args.length > 0) {
    console.log(`Hello, ${Deno.args[0]}!`);
} else {
    console.log("Hello, world!");
}
