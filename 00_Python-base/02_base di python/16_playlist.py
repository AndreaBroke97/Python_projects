'''
class Playlist:
    description = "class used to rappresent playlists"
    
    def __init__(self, name, pl_descr, songs = []): #possiamo manipolarlo come vogliamo
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs
        
        
    def __add__(self, other):
        if isinstance(other, Playlist):
            nuovo_nome = self.name + "+" + other.name
            nuova_pldescr = f"Playlist created automatically unendo {self.name} and {other.name}"
            nuove_songs = self.songs + other.songs
            return Playlist(nuovo_nome, nuova_pldescr, nuove_songs)
        else:
            print("i cant sum the element requested")
            return
        
        
#altro metodo speciale STR (string) definisce come si deve comportare un oggetto quando questo stesso 
# viene provato ad essere convertito in una stringa
    def __str__(self):
     
        a = f (tre apici) \nTitle of playlist: {self.name}\n
        {self.pl_descr} \n
        questa playlist contiene esattamente {len(self.songs)} canzoni
        {self.songs}
        (tre apici)
        return a
        

pl1 = Playlist("\nestate 25 ", "le canzoni di quando ho conosciuto Morena", ['maracaibo', 'danza koduro'])
pl2 = Playlist(" estate 23 ", "le canzoni di quando ho conosciuto Alessia", ['volare', 'macarena', 'buoni o cattivi'])

pl2.totaldurate = 35

pl3 = pl1 + pl2

print(pl3.name)
print(pl3.pl_descr)
print(pl3.songs)


pl1 = Playlist("\nestate 25 ", "le canzoni di quando ho conosciuto Morena", ['maracaibo', 'danza koduro'])

print(pl1)
'''