public class string {

    public static void main(String[] args) {

        // immutable string
        String str = "hello world :)";
        System.out.println(str);

        // Mutable StringBuillder

        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" Jeerasak");
        sb.append(" Ananta");
        System.out.println(sb);
        System.out.println(sb.toString());

    }

}
