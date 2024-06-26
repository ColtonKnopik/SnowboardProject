public class Person {

    int height;
    int weight;
    int specificType;
    // 0: any
    // 1: camber
    //2: rocker
    boolean park;
    boolean allMountain;
    int experience;
    double priceLow, priceHigh;

    @Override
    public String toString() {
        return "Person{" +
                "height=" + height +
                ", weight=" + weight +
                ", specificType=" + specificType +
                ", park=" + park +
                ", allMountain=" + allMountain +
                ", experience=" + experience +
                ", priceLow=" + priceLow +
                ", priceHigh=" + priceHigh +
                '}';
    }

    public Person(int height, int weight, int specificType, boolean park, boolean allMountain, int experience, double priceLow, double priceHigh)
    {
        this.height = height;
        this.weight = weight;
        this.specificType = specificType;
        this.park = park;
        this.allMountain = allMountain;
        this.experience = experience;
        this.priceLow = priceLow;
        this.priceHigh = priceHigh;
    }


}
