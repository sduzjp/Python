clc, clear
a=load('data3_6_1.txt');
[u,s,v]=svd(a)   %奇异值分解
ut = u';
ya=s(1:6,1:6)*(ut(1:6,:))*a  %压缩数据
r =0.5+0.5*corrcoef(a)   %计算归一化相关系数
xlswrite('data3_6_2.xlsx', r)
no = find(a(18,:)==0)  %找未评分菜品编号
yb = setdiff([1:11],no)  %已评分菜品编号
ys = a(18, yb)  %已评分的分数
for i = 1:length(no)
    w = r(no(i), yb);  %提出相似度值
    gf(i)=sum(w.*ys)/sum(w);  %计算估计评分
end
gf