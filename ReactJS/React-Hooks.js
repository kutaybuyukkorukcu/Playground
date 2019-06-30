import React from 'react'
import {Card, Row, Input, Text} from './components'
import ThemeContext from './ThemeContext'

export default class Greetings extends React.Component {
  constructor(props) {
    super(props)
    this.state = { 
      name : 'Mary',
      surname : 'Popins',
      width : width.innerWidth
    }   
  }

  componentDidMount() {
    window.addEventListener('resize', this.handleResize)
    document.title = this.state.name + ' ' + this.state.surname
  }

  componentDidUpdate() {
    document.title = this.state.name + ' ' + this.state.surname
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.handleResize)
  }

  handleNameChange(event) {
    this.setState({ name : event.target.value })
  }

  handleSurnameChange(event) {
    this.setState({ surname : event.target.value })
  }

  handleResize() {
    this.setState({ width : innerWidth })
  }

  render() {
    <ThemeContext.Consumer>
      { theme => (
        <Card theme = {theme}>
          <Row label="Name">
            <Input value = {name} onChange = {this.handleNameChange} />
          </Row>
          <Row label="Surname">
            <Input value = {surname} onChange = {this.handleSurnameChange} />
          </Row>
          <Row label="Width">
            <Text>{width}</Text>
          </Row>
        </Card>
      )}
    </ThemeContext.Consumer>
  }
}
