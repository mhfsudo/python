public int sumOneTonN(int i)
{
    int sum = 0;
    //n iterationen
    for(int i = 1; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}

public int gaussFormula(int n)
{
    return (n * (n + 1)) / 2;
}