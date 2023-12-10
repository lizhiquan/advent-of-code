use std::cmp::Ordering;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("Part 1: {}", solve("input.txt", cmp::<Card1>(hand_type(false))));
    println!("Part 2: {}", solve("input.txt", cmp::<Card2>(hand_type(true))));
}

#[derive(PartialEq, PartialOrd)]
enum Hand {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

trait Card {
    fn from_char(c: char) -> Self;
}

#[derive(PartialEq, PartialOrd)]
enum Card1 {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    T,
    J,
    Q,
    K,
    A,
}

impl Card for Card1 {
    fn from_char(c: char) -> Self {
        match c {
            'A' => Self::A,
            'K' => Self::K,
            'Q' => Self::Q,
            'J' => Self::J,
            'T' => Self::T,
            '9' => Self::Nine,
            '8' => Self::Eight,
            '7' => Self::Seven,
            '6' => Self::Six,
            '5' => Self::Five,
            '4' => Self::Four,
            '3' => Self::Three,
            '2' => Self::Two,
            _ => panic!("Unknown card {}", c),
        }
    }
}

#[derive(PartialEq, PartialOrd)]
enum Card2 {
    J,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    T,
    Q,
    K,
    A,
}

impl Card for Card2 {
    fn from_char(c: char) -> Self {
        match c {
            'A' => Self::A,
            'K' => Self::K,
            'Q' => Self::Q,
            'J' => Self::J,
            'T' => Self::T,
            '9' => Self::Nine,
            '8' => Self::Eight,
            '7' => Self::Seven,
            '6' => Self::Six,
            '5' => Self::Five,
            '4' => Self::Four,
            '3' => Self::Three,
            '2' => Self::Two,
            _ => panic!("Unknown card {}", c),
        }
    }
}

fn hand_type(has_joker: bool) -> Box<dyn Fn(&str) -> Hand> {
    Box::new(move |hand| {
        let mut map = HashMap::new();

        for c in hand.chars() {
            *map.entry(c).or_insert(0) += 1;
        }

        if has_joker {
            if let Some(j_value) = map.get(&'J').copied() {
                if j_value != 5 {
                    map.remove(&'J');
                    let max_val_key = map.iter().max_by_key(|(_, &v)| v).unwrap().0;
                    map.entry(*max_val_key).and_modify(|v| *v += j_value);
                }
            }
        }

        match map.len() {
            1 => Hand::FiveOfAKind,
            2 => {
                if map.values().find(|&x| *x == 1).is_some() {
                    return Hand::FourOfAKind;
                }
                Hand::FullHouse
            }
            3 => {
                if map.values().find(|&x| *x == 3).is_some() {
                    return Hand::ThreeOfAKind;
                }
                Hand::TwoPair
            }
            4 => Hand::OnePair,
            5 => Hand::HighCard,
            _ => panic!(),
        }
    })
}

fn cmp<C>(hand_type: Box<dyn Fn(&str) -> Hand>) -> Box<dyn Fn(&str, &str) -> Ordering>
    where C: Card + PartialEq + PartialOrd {
    Box::new(move |a, b| {
        let hand_a = hand_type(a);
        let hand_b = hand_type(b);

        if hand_a < hand_b {
            return Ordering::Less;
        } else if hand_a > hand_b {
            return Ordering::Greater;
        }

        for i in 0..a.len() {
            let card_a = C::from_char(a.chars().nth(i).unwrap());
            let card_b = C::from_char(b.chars().nth(i).unwrap());
            if card_a < card_b {
                return Ordering::Less;
            } else if card_a > card_b {
                return Ordering::Greater;
            }
        }

        Ordering::Equal
    })
}

fn solve(path: &str, cmp: Box<dyn Fn(&str, &str) -> Ordering>) -> u32 {
    let file = File::open(path).unwrap();
    let mut inputs: Vec<(String, u32)> = BufReader::new(file)
        .lines()
        .filter_map(Result::ok)
        .map(|line| {
            let mut part = line.split(' ');
            let hand = part.next().unwrap().to_owned();
            let bid = part.next().unwrap().to_owned().parse::<u32>().unwrap();
            (hand, bid)
        })
        .collect();

    inputs.sort_by(|a, b| cmp(&a.0, &b.0));

    inputs.iter()
        .enumerate()
        .map(|(i, (_, bid))| (i + 1) as u32 * bid)
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1() {
        assert_eq!(solve("input_test.txt", cmp::<Card1>(hand_type(false))), 6440);
    }

    #[test]
    fn part2() {
        assert_eq!(solve("input_test.txt", cmp::<Card2>(hand_type(true))), 5905);
    }
}
