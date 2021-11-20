use std::io;
use std::io::Write;

fn main() {
    print!("badchars = (\"");
    io::stdout().flush().unwrap();
    for number in 0..256{
        print!("\\x{:02x}", number);
        if number > 15 && number % 16 == 0{
            println!("\\");
        }
        io::stdout().flush().unwrap();
    }
    println!("\")");
}
