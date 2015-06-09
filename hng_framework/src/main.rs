extern crate hng_framework;

use hng_framework::node;
use hng_framework::node::light::Light;

struct MiLight{
    state: bool,
}

impl node::Node for MiLight{
    fn start() {
        println!("Starting node");
    }
}

impl node::light::Light for MiLight {

    fn set_onoff(&mut self, state: bool) {
            self.state = state;
    }

}

fn main() {

    println!("{:?}", hng_framework::node::test());

    println!("{:?}", hng_framework::node::light::test());

    let mut milight = MiLight{state: false};

    milight.set_onoff(true);

    println!("{}", milight.state);
}
