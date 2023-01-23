package domain;

public class Conjured extends NormalItem {

    public Conjured(String name, int sell_in, int quality) {
        super(name, sell_in, quality);
    }

    @Override
    public void updateQuality() {
        if (getQuality() > 0) {
            computeQuality(-2);
        } else {
            computeQuality(-4);
        }
        setSell_in();
    }
}
