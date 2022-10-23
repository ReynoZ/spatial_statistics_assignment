% plot for varogram of irregularly spacing data
clear;
load gamv_out.txt;
h=gamv_out(:,2);
gam=gamv_out(:,3);
% plot(h,gam,'o')

N=12;% number of lags
M=3;%number of directions
figure
% for 1st var.
subplot(121)
hold on
for i=1:M
    hi=h((i-1)*N+1:i*N);
    gami=gam((i-1)*N+1:i*N);
    plot(hi,gami,'DisplayName',['direction ', num2str(i)],'linewidth',3);
end
xlabel('lag distance (h)')
ylabel('\gamma (h)')
xlim([0 max(hi)])
text(17,1.9,'primary varaible','Fontsize',14)
legend('show')
box on
set(gca,'fontsize',20,'fontname','Times')

% for 2nd var.
subplot(122)
hold on
K=M*N;
for i=1:M
    hi=h((i-1)*N+1+K:i*N+K);
    gami=gam((i-1)*N+1+K:i*N+K);
    plot(hi,gami,'DisplayName',['direction ', num2str(i)],'linewidth',3);
end
xlabel('lag distance (h)')
ylabel('\gamma (h)')
xlim([0 max(hi)])
text(17,48,'second varaible','Fontsize',14)
legend('show')
box on
set(gca,'fontsize',20,'fontname','Times')
