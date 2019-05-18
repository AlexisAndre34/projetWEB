public abstract class Pokemon {
    private String name;
    private int poids;
    public Pokemon(String name, int poids);
    public void getName();

    public void setName(String name){
        this.name=name
    }

    public void getPoids();

    public void SetPoids(int poids){
        poids=poids
    }


    abstract vitesse();
    

}
