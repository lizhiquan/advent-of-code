use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}

fn part1() -> u32 {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    let schematic = reader.lines()
        .map(|line| line.unwrap())
        .collect::<Vec<String>>();
    let mut numbers: Vec<u32> = Vec::new();

    for i in 0..schematic.len() {
        let mut j = 0;
        while j < schematic[i].len() {
            if schematic[i].chars().nth(j).unwrap().is_digit(10) {
                // go from j, find last index of the number
                let mut k = j;
                while k < schematic[i].len() && schematic[i].chars().nth(k).unwrap().is_digit(10) {
                    k += 1;
                }

                let number: u32 = schematic[i][j..k].parse().unwrap();

                // check adjacent cells for any symbol ( not '.')
                // top
                if i > 0 {
                    let top = &schematic[i - 1];
                    let from = j.checked_sub(1).unwrap_or(0);
                    let to = k.min(top.len() - 1);
                    if top[from..=to].chars().any(|c| c != '.') {
                        numbers.push(number);
                        j = k;
                        continue;
                    }
                }
                // bottom
                if i < schematic.len() - 1 {
                    let bottom = &schematic[i + 1];
                    let from = j.checked_sub(1).unwrap_or(0);
                    let to = k.min(bottom.len() - 1);
                    if bottom[from..=to].chars().any(|c| c != '.') {
                        numbers.push(number);
                        j = k;
                        continue;
                    }
                }
                // left
                if j > 0 && schematic[i].chars().nth(j - 1).unwrap() != '.' {
                    numbers.push(number);
                    j = k;
                    continue;
                }
                // right
                if k < schematic[i].len() && schematic[i].chars().nth(k).unwrap() != '.' {
                    numbers.push(number);
                    j = k;
                    continue;
                }

                j = k;
            }

            j += 1;
        }
    }

    // println!("{:?}", numbers);
    numbers.iter().sum()
}

fn part2() -> u32 {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    let schematic = reader.lines()
        .map(|line| line.unwrap())
        .collect::<Vec<String>>();

    // gear position -> numbers
    let mut map = HashMap::new();

    for i in 0..schematic.len() {
        let mut j = 0;
        while j < schematic[i].len() {
            if schematic[i].chars().nth(j).unwrap().is_digit(10) {
                // go from j, find last index of the number
                let mut k = j;
                while k < schematic[i].len() && schematic[i].chars().nth(k).unwrap().is_digit(10) {
                    k += 1;
                }

                let number: u32 = schematic[i][j..k].parse().unwrap();

                // check adjacent cells for any symbol ( not '.')
                // top
                if i > 0 {
                    let top = &schematic[i - 1];
                    let from = j.checked_sub(1).unwrap_or(0);
                    let to = k.min(top.len() - 1);
                    for l in from..=to {
                        if top.chars().nth(l).unwrap() == '*' {
                            map.entry((i - 1, l))
                                .or_insert_with(Vec::new)
                                .push(number);
                        }
                    }
                }
                // bottom
                if i < schematic.len() - 1 {
                    let bottom = &schematic[i + 1];
                    let from = j.checked_sub(1).unwrap_or(0);
                    let to = k.min(bottom.len() - 1);
                    for l in from..=to {
                        if bottom.chars().nth(l).unwrap() == '*' {
                            map.entry((i + 1, l))
                                .or_insert_with(Vec::new)
                                .push(number);
                        }
                    }
                }
                // left
                if j > 0 && schematic[i].chars().nth(j - 1).unwrap() == '*' {
                    map.entry((i, j - 1))
                        .or_insert_with(Vec::new)
                        .push(number);
                }
                // right
                if k < schematic[i].len() && schematic[i].chars().nth(k).unwrap() == '*' {
                    map.entry((i, k))
                        .or_insert_with(Vec::new)
                        .push(number);
                }

                j = k;
            }

            j += 1;
        }
    }

    map.iter()
        .filter(|(_, v)| v.len() == 2)
        .map(|(_, v)| v[0] * v[1])
        .sum()
}