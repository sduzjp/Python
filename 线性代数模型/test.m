clc, clear
a=load('data3_6_1.txt');
[u,s,v]=svd(a)   %����ֵ�ֽ�
ut = u';
ya=s(1:6,1:6)*(ut(1:6,:))*a  %ѹ������
r =0.5+0.5*corrcoef(a)   %�����һ�����ϵ��
xlswrite('data3_6_2.xlsx', r)
no = find(a(18,:)==0)  %��δ���ֲ�Ʒ���
yb = setdiff([1:11],no)  %�����ֲ�Ʒ���
ys = a(18, yb)  %�����ֵķ���
for i = 1:length(no)
    w = r(no(i), yb);  %������ƶ�ֵ
    gf(i)=sum(w.*ys)/sum(w);  %�����������
end
gf