use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
}

struct Game {
    id: u32,
    sets: Vec<GameSet>,
}

impl Game {
    fn from(input: &str) -> Option<Game> {
        let parts: Vec<&str> = input.split(": ").collect();

        if parts.len() != 2 {
            return None;
        }

        let id: u32 = parts[0].trim_start_matches("Game ").parse().ok()?;
        let sets: Vec<GameSet> = parts[1].split("; ").
            filter_map(GameSet::from).
            collect();
        Some(Game { id, sets })
    }

    fn is_valid(&self, max_red: u32, max_green: u32, max_blue: u32) -> bool {
        self.sets.iter()
            .all(|set|
                set.red <= max_red && set.green <= max_green && set.blue <= max_blue
            )
    }

    fn fewest_cubes(&self) -> GameSet {
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        for set in &self.sets {
            red = red.max(set.red);
            green = green.max(set.green);
            blue = blue.max(set.blue);
        }

        GameSet { red, green, blue }
    }
}

#[derive(Default)]
struct GameSet {
    red: u32,
    green: u32,
    blue: u32,
}

impl GameSet {
    fn from(input: &str) -> Option<GameSet> {
        let mut set = GameSet::default();

        let parts: Vec<&str> = input.split(", ").collect();
        for part in parts {
            let number_and_color: Vec<&str> = part.split(" ").collect();
            if number_and_color.len() != 2 {
                return None;
            }
            let n: u32 = number_and_color[0].parse().ok()?;
            match number_and_color[1] {
                "red" => set.red = n,
                "green" => set.green = n,
                "blue" => set.blue = n,
                _ => {}
            }
        }

        Some(set)
    }

    fn power(&self) -> u32 {
        self.red * self.green * self.blue
    }
}

fn part1() -> u32 {
    let red = 12;
    let green = 13;
    let blue = 14;

    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    reader.lines()
        .filter_map(Result::ok)
        .filter_map(|line| Game::from(&line))
        .filter(|game| game.is_valid(red, green, blue))
        .map(|game| game.id)
        .sum()
}

fn part2() -> u32 {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    reader.lines()
        .filter_map(Result::ok)
        .filter_map(|line| Game::from(&line))
        .map(|game| game.fewest_cubes().power())
        .sum()
}
