# Instale, se ainda não tiver:
# install.packages(c("readr","dplyr"))

library(readr)
library(dplyr)

# 1) Leitura do arquivo (CSV):
df <- read_csv("CompanhiaMB_limpo.csv", na = c("?", ""))

# Se for Excel:
# library(readxl)
# df <- read_excel("seu_arquivo.xlsx", na = c("?", ""))

# 2) Cálculo das estatísticas para x e y
stats <- df %>%
  summarise(
    across(
      c(x, y),
      list(
        media     = ~mean(.x, na.rm = TRUE),
        variancia = ~var(.x, na.rm = TRUE),
        dp        = ~sd(.x, na.rm = TRUE),
        mediana   = ~median(.x, na.rm = TRUE)
      ),
      .names = "{.col}_{.fn}"
    )
  )

print(stats)
