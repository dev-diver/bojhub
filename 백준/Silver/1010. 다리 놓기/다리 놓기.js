[N,...L]=(require('fs').readFileSync(0)+"").trim().split`
`
console.log(L.map(e=>{
  [N,M]=e.split` `.map(e=>+e)
  let p=1n
  for(let i=M;i>N;i--){
    p*=BigInt(i)
  }
  for(let i=M-N;i>1;i--){
    p/=BigInt(i)
  }
  return p
}).join('\n'))