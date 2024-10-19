import logoImg from '../../assets/logo.svg';
import { Container, Content } from './styles';


export function Header() {

  return (
    <Container>
      <Content>
        {/* <img src={logoImg} alt="dt money" /> */}
        <h1>BandecoPay</h1>
        <button type="button">
            Login
        </button>
      </Content>
    </Container>
  );
}