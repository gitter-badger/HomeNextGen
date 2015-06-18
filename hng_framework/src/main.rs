pub mod device;

use device::channel::{OnOff, Brightness};

struct MiLight{
    state: bool,
    brightness: i32,
}

impl device::Light for MiLight{}

impl device::channel::OnOff for MiLight{
    fn set_onoff(&self, val: bool) {
        println!("Starting onoff");
    }

    fn get_onoff(&self, val: bool){
        println!("Getting onoff");
    }
}

impl device::channel::Brightness for MiLight{
    fn set_brightness(&self, brightness: i32){
        println!("Brightness = {}", brightness);
    }

    fn get_brightness(&self, brightness: i32){
        println!("Brightness = {}", brightness);
    }
}


fn main() {

    let mut milight = MiLight{state: false, brightness: 0};

    milight.set_brightness(100);


    println!("{}", milight.state);
}
