import click
import tpSCAN


@click.command()
@click.option('--name', prompt='Dataset name(str)', help='The name of the loaded dataset')
@click.option('--eps', prompt='Epsilon(float)', help='The value of the parameter Epsilon')
@click.option('--tau', prompt='Tau(int)', help='The value of the parameter Tau')
@click.option('--miu', prompt='Miu(int)', help='The value of the parameter Miu')
@click.option('--method', prompt='Type one number to chose the algorithm: [1]TSCANB; [2]TSACNS; [3]TSCANA. (int)', help='Three stable community detection methods')
def doit(name, eps, miu, tau, method):
    eps = float(eps)
    miu = int(miu)
    tau = int(tau)
    G = tpSCAN.tGraph(name)
    if method is "1":
        G.SCANB(miu,tau,eps)
    if method is "2":
        G.SCANS(miu,tau,eps)
    if method is "3":
        G.SCANA(miu,tau,eps)

if __name__ == '__main__':
    doit()