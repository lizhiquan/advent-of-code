use std::fs::read_to_string;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let content = read_to_string("input.txt").unwrap();
    let mut lines = content.lines();
    let times = lines.next().unwrap()
        .trim_start_matches("Time:")
        .split_whitespace()
        .filter_map(|x| x.parse::<u32>().ok())
        .collect::<Vec<u32>>();
    let distances = lines.next().unwrap()
        .trim_start_matches("Distance:")
        .split_whitespace()
        .filter_map(|x| x.parse::<u32>().ok())
        .collect::<Vec<u32>>();

    times.iter().zip(distances.iter())
        .map(|(time, distance)| {
            (1..=*time)
                .map(|i| (time - i) * i)
                .filter(|d| d > distance)
                .count() as u32
        })
        .product()
}

fn part2() -> u64 {
    let content = read_to_string("input.txt").unwrap();
    let mut lines = content.lines();
    let time = lines.next().unwrap()
        .trim_start_matches("Time:")
        .chars()
        .filter(|&c| !c.is_whitespace())
        .collect::<String>()
        .parse::<u64>()
        .unwrap();
    let distance = lines.next().unwrap()
        .trim_start_matches("Distance:")
        .chars()
        .filter(|&c| !c.is_whitespace())
        .collect::<String>()
        .parse::<u64>()
        .unwrap();

    (1..=time)
        .map(|i| (time - i) * i)
        .filter(|&d| d > distance)
        .count() as u64
}
