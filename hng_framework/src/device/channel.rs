

pub trait OnOff{
    fn set_onoff(&self, status: bool);
    fn get_onoff(&self, status: bool);
}


pub trait Brightness{
    fn set_brightness(&self, val: i32);
    fn get_brightness(&self, val: i32);
}
