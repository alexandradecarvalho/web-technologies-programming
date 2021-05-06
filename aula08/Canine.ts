import {Mammal} from './Mammal'

export class Canine extends Mammal{
    static nCanines: number = 0;
    race : string;

    constructor(habitat: string, race: string) {
        super(habitat);
        this.race = race;
        Canine.nCanines++;
    }
}