
import java.util.List;
import domain.*;

public class App {
    public static void main(String[] args) {
        System.out.println("Welcome to Gilded Rose Kata!");

        GildedRose shop = new GildedRose();

        List<Updateable> items = List.of(new NormalItem("+5 Dexterity Vest", 10, 20),
                new AgedBrie("Aged Brie", 2, 0),
                new NormalItem("Elixir of the Mongoose", 5, 7),
                new Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                new Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                new Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                new Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49),
                new Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49));

        for (Updateable item : items) {
            shop.addItem(item);
        }

        System.out.println("\t #### Day 1 ####");
        System.out.println(shop.toString());

        shop.updateQuality();

        System.out.println("\t #### Day 2 ####");
        System.out.println(shop.toString());

        shop.addItem(new NormalItem("Sword", 20, 20));
        shop.addItem(new Conjured("Conjured Mana Cake", 3, 6));

        System.out.println("\t #### New normal item sword added ####");
        System.out.println("\t #### New item conjured added ####");
        System.out.println(shop.toString());

        shop.updateQuality();
        System.out.println("\t #### Day 3 ####");
        System.out.println(shop.toString());
    }

}
