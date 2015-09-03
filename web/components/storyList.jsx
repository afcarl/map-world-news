'use strict';

const React = require('react')
const Story = require('./story.jsx')

module.exports = React.createClass({
  render: function() {
    return <div id={this.props.id} className="story-list col-sm-12 col-md-12">
      <h3>{this.props.title}</h3>
      <div className="row">
      {this.props.stories ?
        this.props.stories.map(function(story) {
          return <Story {...story} />
        })
      : 'No Stories'}
      </div>
    </div>;
  }
});