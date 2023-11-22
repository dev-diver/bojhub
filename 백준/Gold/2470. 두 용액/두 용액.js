var fs = require('fs');
r = fs.readFileSync('dev/stdin').toString().split('\n')
N = +r[0]
nums = r[1].split(' ').map(a=>+a)
nums.sort((a,b)=>a-b)
i=0
j=N-1
min=10000000000
mina=[nums[i],nums[j]]
while(i<j){
  sum=nums[i]+nums[j]
  if(Math.abs(sum)<min){
    mina[0]=nums[i]
    mina[1]=nums[j]
    min=Math.abs(sum)
  }
  if(sum<0){
    i+=1
  }else{
    j-=1
  }
}
console.log(mina[0],mina[1])