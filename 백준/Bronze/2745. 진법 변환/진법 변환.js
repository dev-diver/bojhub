[S,n]=(require('fs').readFileSync(0)+"").split` `
D="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".split``
console.log(S.split``.reverse().reduce((a,c)=>[a[0]+D.indexOf(c)*n**a[1],a[1]+1],[0,0])[0])