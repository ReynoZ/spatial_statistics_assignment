% plot for varogram of grided data
clear;
load gam_out.txt;
h=gam_out(:,2);
gam=gam_out(:,3);

N=10;% number of lags
M=2;%number of directions

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
text(0.5,27.5,'primary varaible','Fontsize',16)
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
text(0.5,7.5,'second varaible','Fontsize',16)
legend('show')
box on
set(gca,'fontsize',20,'fontname','Times')
