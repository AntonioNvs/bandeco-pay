import { Container, DashboardContainer} from './styles';

export function Dashboard() {

    // A ideia é buscar os cardápios do dia de uma API
    const menuItems = [
        "Arroz Branco",
        "Assado de Grão-de-Bico",
        "Banana Nanica",
        "Feijão Carioca",
        "Frango Xadrez",
        "Molho Verde",
        "Penne ao Manjericão",
        "Refresco",
        "Salada de Alface",
        "Salada de Tomate"
      ];
    return (
        <Container>
            <DashboardContainer>
            {/* Quatro cardápios (colunas) */}
                {[...Array(4)].map((_, index) => (
                    <div className="menu-card" key={index}>
                    <h2>Restaurante universitário {index + 1}</h2>
                    <ul>
                        {menuItems.map((item, idx) => (
                        <li key={idx}>{item}</li>
                        ))}
                    </ul>
                    </div>
                ))}
            </DashboardContainer>
        </Container>
    );
}