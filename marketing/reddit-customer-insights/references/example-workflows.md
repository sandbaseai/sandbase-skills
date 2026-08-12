# Example Workflows

Each example uses SandBase Reddit capabilities as the evidence source. Inspect the current schema with `sandbase_describe_tool` before calling any listed tool.

## 1. Pain point discovery for a product category

**User request**

```text
Find recurring pain points for project-management software buyers on Reddit.
```

**Use these capabilities**

1. `reddit_app_search_typeahead` with queries: "project management software", "project management tool", "PM tool recommendation".
2. `reddit_app_dynamic_search` with queries: "frustrated project management", "project management tool problems", "looking for alternative to [top tools]".
3. `reddit_app_topic_feed` for r/projectmanagement and r/ProductManagement.
4. `reddit_app_post_details` for the top 5–8 high-engagement posts.

**Return**: pain points ranked by frequency (e.g., "too complex for small teams" — 12 posts, "poor mobile experience" — 8 posts), with representative quotes and community context.

## 2. Buying triggers and decision research

**User request**

```text
What events or needs prompt teams to look for a new CRM? Find buying triggers from Reddit.
```

**Use these capabilities**

1. `reddit_app_search_typeahead` with: "CRM recommendation", "new CRM", "switching CRM".
2. `reddit_app_dynamic_search` with: "outgrew our CRM", "need new CRM because", "switching from Salesforce", "CRM for small team".
3. `reddit_app_post_details` for posts that describe the decision moment.

**Return**: buying triggers ranked (e.g., "team size outgrew current tool", "pricing increased", "needed better integrations"), each with 2+ source posts and the context of who's buying.

## 3. Competitive switching intelligence

**User request**

```text
Why are people switching away from [Competitor]? What are they switching to?
```

**Use these capabilities**

1. `reddit_app_dynamic_search` with: "switched from [Competitor]", "leaving [Competitor]", "alternative to [Competitor]", "[Competitor] vs".
2. `reddit_app_post_details` for detailed switching stories.
3. `reddit_app_topic_feed` for the competitor's subreddit (if public).

**Return**: a switching reasons table (reason, frequency, example quote), a destinations table (what they switched to and why), and signals about what would make them stay.

## 4. Customer language extraction for marketing

**User request**

```text
How do developers describe their frustrations with API documentation? I need their exact language for our messaging.
```

**Use these capabilities**

1. `reddit_app_search_typeahead` with: "API documentation", "API docs frustrating".
2. `reddit_app_dynamic_search` across r/programming, r/webdev, r/ExperiencedDevs with queries about documentation frustrations.
3. `reddit_app_post_details` for high-comment threads.

**Return**: a language bank organized by frustration type, with exact phrases (paraphrased to avoid doxing), frequency indicators, and suggested messaging angles that use customer vocabulary.

## 5. Content opportunity discovery

**User request**

```text
Find unanswered questions about [topic] on Reddit that we could create content for.
```

**Use these capabilities**

1. `reddit_app_search_typeahead` to find relevant communities.
2. `reddit_app_dynamic_search` with question-format queries: "how to [topic]", "best way to [topic]", "help with [topic]".
3. `reddit_app_post_details` for posts with many comments but no clear resolution.

**Return**: a prioritized list of content opportunities, each with the original question, community, engagement level, existing answer quality (poor/none/partial), and a suggested content angle.
