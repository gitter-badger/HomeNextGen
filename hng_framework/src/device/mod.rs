pub mod channel;

pub trait Light: channel::OnOff + channel::Brightness{}

pub fn test(){
    println!("Hello Light");
}
