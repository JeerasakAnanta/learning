fn hell(s:String){
    println!("Hello, world! {} ",s);
}
fn main() {
    let  s1 =  "GAME! ;)".to_string();

    // call function
    hell(s1.clone());

    print!("{ }",s1);

}
