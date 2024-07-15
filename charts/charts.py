import matplotlib.pyplot as plt

def generated_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    data = [200, 300, 400, 500]

    fig,ax = plt.subplots()
    ax.pie(data, labels=labels)
    ax.axis('equal')
    #Generar una imagen y no usar show.
    plt.savefig('pie.png')

    plt.close()


