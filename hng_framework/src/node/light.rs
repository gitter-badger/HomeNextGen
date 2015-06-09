pub trait Light{
    fn set_onoff(&mut self, state: bool);

    fn get_onoff(state: bool){
        println!("Default. Not implemented");
    }

    fn set_brightness(brightness: i32){
        println!("Default. Not implemented");
    }

    fn get_brightness(brightness: i32){
        println!("Default. Not implemented");
    }

    fn set_color(r: i32, g: i32, b: i32){
        println!("Default. Not implemented");
    }

    fn get_color(r: i32, g: i32, b: i32){
        println!("Default. Not implemented");
    }
}

pub fn test(){
    println!("Hello Light");
}
