#创建均值为0、标准差为1的标准正态随机变量
set.seed(1303)
x <- rnorm(50)
mean(x) #均值
var(x) #方差
sqrt(var(x)) #标准差
sd(x) #标准差

y <- rnorm(50)
plot(x,y)
plot(x, y, xlab ="this is the x-axis",
     ylab ="this is the y-axis",
     main ="Plot of X vs Y")

#保存为PDF
pdf("Figure.pdf")
plot(x, y, col ="green")
dev.off() #表明绘图完毕


seq(1, 10) #类似于, 产生1到10的整数
x <- 1:10
seq(0, 1, length = 10) #在0到1之间产生10个等间距的数
x <- seq(-pi, pi, length = 50)
x

#等高线图
y <- x
f <-outer(x, y,function(x, y)cos(y) / (1 + x^2))
contour(x, y, f)
contour(x, y, f, nlevels = 45, add = T)
fa <- ( f -t(f)) / 2
contour(x, y, fa, nlevels = 15)
#热图
image(x, y, fa)
#三维图
persp(x, y, fa)
persp(x, y, fa, theta = 30) #水平旋转30°
persp(x, y, fa, theta = 30, phi = 20) #垂直方向再旋转20°
persp(x, y, fa, theta = 30, phi = 70)
persp(x, y, fa, theta = 30, phi = 40)

setwd("F:/刘晖老师/教科书/islr")
Auto <-read.table("Auto.data")
head(Auto)
Auto <-read.table("Auto.data", header = T , na.strings="?", #？是NA
                      stringsAsFactors = T) #字符串是定性变量
Auto <-read.csv("Auto.csv", na.strings ="?",
                    stringsAsFactors = T)
dim(Auto)
Auto[ 1 : 4, ]
Auto <-na.omit(Auto) #删除有缺失值的行
dim(Auto)
names(Auto)

plot(Auto$cylinders , Auto$mpg)
#或者
attach(Auto)
plot(cylinders , mpg)
cylinders <-as.factor(cylinders) #cylinders可以认为是定性数据
plot(cylinders , mpg) #x是定性变量，plot箱型图
plot(cylinders , mpg, col ="red")
plot(cylinders , mpg, col ="red", varwidth = T ) #箱子的宽度随数据量变化
plot(cylinders , mpg, col ="red", varwidth = T ,
     horizontal = T) #箱型图变为水平的
plot(cylinders , mpg, col ="red", varwidth = T ,
     xlab ="cylinders", ylab ="MPG")

#直方图
hist(mpg)
hist(mpg, col = 2)
hist(mpg, col = 2, breaks = 15)

#散点图矩阵 两个变量之间画散点图
pairs(Auto)

#交互式的讲图上的点给出特定的值
plot(horsepower , mpg)
identify(horsepower , mpg, name) #第三个输入是想要在图上输出的点的什么信息
#identify的输出是标记点所在的行

summary(Auto)
summary(mpg)
range(Auto$mpg)
range(Auto$cylinders)
auto1 <- Auto[-(10:85),]
summary(auto1)

college <- read.csv("College.csv",header = TRUE)
rownames(college) <- college[, 1]
college <- college[ , - 1 ]
View(college)

summary(college)
a=college[,2:10]
pairs(a)
college$Private=as.factor(college$Private)
plot(college$Private,college$Outstate)
Elite <-rep("No",nrow(college))
Elite[ college$Top10perc > 50 ] <-"Yes"
Elite<-as.factor(Elite)
college<-data.frame(college , Elite)
summary(college$Elite)
plot(college$Elite,college$Outstate)

install.packages("ISLR2")
library(ISLR2)
Boston 
?Boston
dim(Boston)
pairs(Boston)
summary(Boston$rm)
boston_h <- Boston[which(Boston$rm > 8),] 
dim(boston_h)
View(boston_h)
summary(boston_h)

boston_g <- Boston[which(Boston$medv==min(Boston$medv)),]
boston_g
boston_g[3,] <- c(mean(Boston$crim),mean(Boston$zn),mean(Boston$indus),mean(Boston$chas),
                  mean(Boston$nox),mean(Boston$rm),mean(Boston$age),
                  mean(Boston$dis),mean(Boston$rad),mean(Boston$tax),mean(Boston$ptratio),
                  mean(Boston$lstat),mean(Boston$medv))
boston_g
summary(Boston$ptratio)
boston_e <- Boston[which(Boston$chas==1),]
dim(boston_e)
boston_d <- Boston[which(Boston$crim==max(Boston$crim)),]
boston_d
