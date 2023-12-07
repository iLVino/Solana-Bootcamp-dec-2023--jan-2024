fn fizzbuzz() {
    let mut fizzbuzz_count = 0;
    for i in 1..=301 {
       match i {
        n if n % 3 == 0 && n % 5 == 0 => {
               println!("fizz buzz");
               fizzbuzz_count += 1;
           }
           n if n % 3 == 0 => println!("fizz"),
           n if n % 5 == 0 => println!("buzz"),
           _ => (),
       } 
    }
    println!("fizzbuzz occurrences: {}", fizzbuzz_count);
}
fn main() {
    println!("Running fizzbuzz!");
    fizzbuzz();
}
