use std::fs::File;
use std::io::{self, BufRead};

fn process_line(line: &str) -> u32 {
    let first_digit = line.chars().find(|&c| c.is_digit(10)).unwrap();
    let last_digit = line.chars().rev().find(|&c| c.is_digit(10)).unwrap();

    let two_digit_number: u32 = format!("{}{}", first_digit, last_digit).parse().unwrap();

    two_digit_number
}

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = io::BufReader::new(file);

    let total_sum: u32 = reader
        .lines()
        .filter_map(|line| line.ok())
        .map(|line| process_line(&line))
        .sum();

    println!("Total sum: {}", total_sum);

    Ok(())
}
